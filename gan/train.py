import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lr",
                        type=float,
                        default=0.0002)
    parser.add_argument("--beta1",
                        type=float,
                        default=0.5)
    parser.add_argument("--beta2",
                        type=float,
                        default=0.999)
    parser.add_argument("--lambda1",
                        type=int,
                        default=100)
    parser.add_argument("--batch_size",
                        type=int,
                        default=64)
    parser.add_argument("--max_epochs",
                        type=int,
                        default=500)
    parser.add_argument("action",
                        choices=("stage1", "stage2"))
    parser.add_argument("--cuda",
                        action="store_true")
    parser.add_argument("--dataset_dir",
                        type=str,
                        default="dataset/")
    parser.add_argument("--model_dir",
                        type=str,
                        default="model/")

    return parser.parse_args()


def main(config):
    t = trainer.Trainer(config)
    if config.action == "stage2":
        t.load_stage1(os.path.join(config.model_dir, "stage1"))
    t.fit()


if __name__ == "__main__":
    config = parse_args()
    config.is_train = True

    if config.action == "stage1":
        import stage1.trainer as trainer
    elif config.action == "stage2":
        import stage2.trainer as trainer

    main(config)
