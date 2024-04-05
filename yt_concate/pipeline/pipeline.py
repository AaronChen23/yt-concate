from .steps.step import StepException
class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                # step.process(inputs) -->這個只有執行第一步驟而已，要有"交手"步驟，把前一步驟資料"交手"到下一步驟(如下一行範例程式+data)
                data = step.process(data, inputs, utils)
            except StepException as e:
                print("Exception happened:", e)
                break