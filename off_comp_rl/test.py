from absl import app, flags
import numpy as np
from offline_env_with_envs import MTLOfflineCompoSuiteEnv
import json

def main(_):
    offline_kwargs = {"ref_min_score": 0, "ref_max_score": 500, "dataset_url": ""}
    with open("train_test_splits/single_task/split_0.json", "r") as f:
        train_task_list = json.load(f)["train"]
    env = MTLOfflineCompoSuiteEnv(
            max_parallel_envs=1,
            task_list=train_task_list,
            **({"offline_kwargs": offline_kwargs})
        )
    state = env.reset()

if __name__ == "__main__":
    app.run(main)