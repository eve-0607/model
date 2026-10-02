#!/usr/bin/env python3
from __future__ import annotations
import json, platform, sys

def main() -> None:
    report = {"python": sys.version, "platform": platform.platform()}
    try:
        import torch
        report.update({
            "torch": torch.__version__,
            "cuda_available": torch.cuda.is_available(),
            "cuda_version": torch.version.cuda,
            "gpu_count": torch.cuda.device_count(),
            "gpus": [torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())],
        })
    except Exception as exc:
        report["torch_error"] = repr(exc)
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
