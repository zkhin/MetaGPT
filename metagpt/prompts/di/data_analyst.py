from metagpt.strategy.task_type import TaskType

EXTRA_INSTRUCTION = """
6. Carefully choose to use or not use the browser tool to assist you in web tasks. 
    - When no click action is required, no need to use the Browser tool to navigate to the webpage before scraping.
    - Write code to view the HTML content rather than using the Browser tool.
    - Make sure the command_name are certainly in Available Commands when you use the Browser tool.
7. When you are making plan. It is highly recommend to plan and append all the tasks in first response once time.
8. Don't finish_current_task multiple times for the same task. 
9. Finish current task timely, such as when the code is written and executed successfully.
"""

TASK_TYPE_DESC = "\n".join([f"- **{tt.type_name}**: {tt.value.desc}" for tt in TaskType])


CODE_STATUS = """
**Code written**:
{code}

**Execution status**: {status}
**Execution result**: {result}
"""
