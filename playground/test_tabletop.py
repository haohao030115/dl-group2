from pathlib import Path
import time

import mujoco
import mujoco.viewer


xml_path = Path(__file__).parent / "tabletop_scene.xml"

model = mujoco.MjModel.from_xml_path(str(xml_path))
data = mujoco.MjData(model)

print("nq =", model.nq)
print("nv =", model.nv)
print("nu =", model.nu)

# 暂时关闭重力：
# 我们现在只是测试 actuator，不希望 G1 没 controller 就直接倒下
model.opt.gravity[:] = [0, 0, 0]

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():

        # 真正推进物理
        mujoco.mj_step(model, data)

        # 更新 GUI
        viewer.sync()

        time.sleep(model.opt.timestep)