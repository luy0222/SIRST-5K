# Copyright (c) OpenMMLab. All rights reserved.
import math

import numpy as np
import torch
from torchvision.utils import make_grid


def tensor2img(tensor, out_type=np.uint8, min_max=(0, 1)):
    if not (torch.is_tensor(tensor) or
            (isinstance(tensor, list)
             and all(torch.is_tensor(t) for t in tensor))):
        raise TypeError(
            f'tensor or list of tensors expected, got {type(tensor)}')

    if torch.is_tensor(tensor):
        tensor = [tensor]
    result = []
    for _tensor in tensor:
        _tensor = _tensor.squeeze(0).squeeze(0)
        _tensor = _tensor.float().detach().cpu().clamp_(*min_max)
        _tensor = (_tensor - min_max[0]) / (min_max[1] - min_max[0])
        n_dim = _tensor.dim()
        if n_dim == 4:
            img_np = make_grid(
                _tensor, nrow=int(math.sqrt(_tensor.size(0))),
                normalize=False).numpy()
            img_np = np.transpose(img_np[[2, 1, 0], :, :], (1, 2, 0))
        elif n_dim == 3:
            img_np = _tensor.numpy()
            img_np = np.transpose(img_np[[2, 1, 0], :, :], (1, 2, 0))
        elif n_dim == 2:
            img_np = _tensor.numpy()
        else:
            raise ValueError('Only support 4D, 3D or 2D tensor. '
                             f'But received with dimension: {n_dim}')
        if out_type == np.uint8:
            # Unlike MATLAB, numpy.unit8() WILL NOT round by default.
            img_np = (img_np * 255.0).round()
        img_np = img_np.astype(out_type)
        result.append(img_np)
    result = result[0] if len(result) == 1 else result
    return result
