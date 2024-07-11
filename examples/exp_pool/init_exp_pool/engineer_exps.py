import json

OBJ1 = [
    {
        "role": "user",
        "content": '\n# Data Structure\n\n\n# Current Plan\n{\'goal\': "Please write a 1024 game using JavaScript and HTML code without using any frameworks, user can play with keyboard. Refer to the system design located at \'/tmp/system_design.json\' and the project schedule at \'/tmp/project_schedule.json\' for detailed information.", \'tasks\': []}\n\n# Current Task\n\n\n# Example\n\n\n# Instruction\nBased on the context, write a plan or modify an existing plan to achieve the goal. A plan consists of one to 3 tasks.\nIf plan is created, you should track the progress and update the plan accordingly, such as Plan.finish_current_task, Plan.append_task, Plan.reset_task, Plan.replace_task, etc.\nWhen presented a current task, tackle the task using the available commands.\nPay close attention to new user message, review the conversation history, use RoleZero.reply_to_human to respond to new user requirement.\nNote:\n1. If you keeping encountering errors, unexpected situation, or you are not sure of proceeding, use RoleZero.ask_human to ask for help.\n2. Carefully review your progress at the current task, if your actions so far has not fulfilled the task instruction, you should continue with current task. Otherwise, finish current task.\n3. Each time you finish a task, use RoleZero.reply_to_human to report your progress.\n4. Each time you write a code in your response, write with the Editor directly without preparing a repetitive code block beforehand.\n5. Take on ONE task and write ONE code file in each response. DON\'T attempt all tasks in one response.\n6. When not specified, you should write files in a folder named "src". If you know the project path, then write in a "src" folder under the project path.\n7. When provided system design or project schedule, you MUST read them first before making a plan, then adhere to them in your implementation, especially in the programming language, package, or framework. You MUST implement all code files prescribed in the system design or project schedule. You can create a plan first with each task corresponding to implementing one code file.\n8. Write at most one file per task, do your best to implement THE ONLY ONE FILE. CAREFULLY CHECK THAT YOU DONT MISS ANY NECESSARY CLASS/FUNCTION IN THIS FILE.\n9. COMPLETE CODE: Your code will be part of the entire project, so please implement complete, reliable, reusable code snippets.\n10. When provided system design, YOU MUST FOLLOW "Data structures and interfaces". DONT CHANGE ANY DESIGN. Do not use public member functions that do not exist in your design.\n11. Write out EVERY CODE DETAIL, DON\'T LEAVE TODO.\n12. To modify code in a file, read the entire file, make changes, and update the file with the complete code, ensuring that no line numbers are included in the final write.\n13. When a system design or project schedule is provided, at the end of the plan, add a CodeRview Task for each file; for example, if there are three files, add three CodeRview Tasks. For each CodeRview Task, just call ReviewAndRewriteCode.run.\n\nPay close attention to the Example provided, you can reuse the example for your current situation if it fits.\nYou may use any of the available commands to create a plan or update the plan. You may output mutiple commands, they will be executed sequentially.\nIf you finish current task, you will automatically take the next task in the existing plan, use Plan.finish_task, DON\'T append a new task.\n\n# Your commands in a json array, in the following output format. If there is nothing to do, use the pass or end command:\nSome text indicating your thoughts, such as how you should update the plan status, respond to inquiry, or seek for help. Then a json array of commands. You must output ONE and ONLY ONE json array. DON\'T output multiple json arrays with thoughts between them.\n```json\n[\n    {\n        "command_name": str,\n        "args": {"arg_name": arg_value, ...}\n    },\n    ...\n]\n```\nNotice: your output JSON data section must start with **```json [**\n',
    }
]
OBJ2 = [
    {
        "role": "user",
        "content": "Command Editor.read executed: file_path='/tmp/system_design.json' block_content=\"...\"\n\nCommand Editor.read executed: file_path='/tmp/project_schedule.json' block_content=\"...\"",
    },
    {
        "role": "user",
        "content": '\n# Data Structure\n\n\n# Current Plan\n{\'goal\': "Please write a 1024 game using JavaScript and HTML code without using any frameworks, user can play with keyboard. Refer to the system design located at \'/tmp/system_design.json\' and the project schedule at \'/tmp/project_schedule.json\' for detailed information.", \'tasks\': []}\n\n# Current Task\n\n\n# Example\n\n\n# Instruction\nBased on the context, write a plan or modify an existing plan to achieve the goal. A plan consists of one to 3 tasks.\nIf plan is created, you should track the progress and update the plan accordingly, such as Plan.finish_current_task, Plan.append_task, Plan.reset_task, Plan.replace_task, etc.\nWhen presented a current task, tackle the task using the available commands.\nPay close attention to new user message, review the conversation history, use RoleZero.reply_to_human to respond to new user requirement.\nNote:\n1. If you keeping encountering errors, unexpected situation, or you are not sure of proceeding, use RoleZero.ask_human to ask for help.\n2. Carefully review your progress at the current task, if your actions so far has not fulfilled the task instruction, you should continue with current task. Otherwise, finish current task.\n3. Each time you finish a task, use RoleZero.reply_to_human to report your progress.\n4. Each time you write a code in your response, write with the Editor directly without preparing a repetitive code block beforehand.\n5. Take on ONE task and write ONE code file in each response. DON\'T attempt all tasks in one response.\n6. When not specified, you should write files in a folder named "src". If you know the project path, then write in a "src" folder under the project path.\n7. When provided system design or project schedule, you MUST read them first before making a plan, then adhere to them in your implementation, especially in the programming language, package, or framework. You MUST implement all code files prescribed in the system design or project schedule. You can create a plan first with each task corresponding to implementing one code file.\n8. Write at most one file per task, do your best to implement THE ONLY ONE FILE. CAREFULLY CHECK THAT YOU DONT MISS ANY NECESSARY CLASS/FUNCTION IN THIS FILE.\n9. COMPLETE CODE: Your code will be part of the entire project, so please implement complete, reliable, reusable code snippets.\n10. When provided system design, YOU MUST FOLLOW "Data structures and interfaces". DONT CHANGE ANY DESIGN. Do not use public member functions that do not exist in your design.\n11. Write out EVERY CODE DETAIL, DON\'T LEAVE TODO.\n12. To modify code in a file, read the entire file, make changes, and update the file with the complete code, ensuring that no line numbers are included in the final write.\n13. When a system design or project schedule is provided, at the end of the plan, add a CodeRview Task for each file; for example, if there are three files, add three CodeRview Tasks. For each CodeRview Task, just call ReviewAndRewriteCode.run.\n\nPay close attention to the Example provided, you can reuse the example for your current situation if it fits.\nYou may use any of the available commands to create a plan or update the plan. You may output mutiple commands, they will be executed sequentially.\nIf you finish current task, you will automatically take the next task in the existing plan, use Plan.finish_task, DON\'T append a new task.\n\n# Your commands in a json array, in the following output format. If there is nothing to do, use the pass or end command:\nSome text indicating your thoughts, such as how you should update the plan status, respond to inquiry, or seek for help. Then a json array of commands. You must output ONE and ONLY ONE json array. DON\'T output multiple json arrays with thoughts between them.\n```json\n[\n    {\n        "command_name": str,\n        "args": {"arg_name": arg_value, ...}\n    },\n    ...\n]\n```\nNotice: your output JSON data section must start with **```json [**\n',
    },
]

REQ1 = json.dumps(OBJ1)
REQ2 = json.dumps(OBJ2)

RESP1 = """
Explanation: To begin the task of creating a 2048 game using JavaScript and HTML, I need to first read the system design and project schedule documents to understand the specific requirements and architecture outlined for the game development.

```json
[
    {
        "command_name": "Editor.read",
        "args": {
            "path": "/tmp/system_design.json"
        }
    },
    {
        "command_name": "Editor.read",
        "args": {
            "path": "/tmp/project_schedule.json"
        }
    }
]
```
"""
RESP2 = """
Explanation: Based on the system design and project schedule, I will create a plan to implement the 2048 game. The plan will consist of tasks to create the necessary files (`index.html`, `style.css`, and `script.js`) and review each file to ensure they meet the design specifications.

Here's the plan:

1. **Task 1**: Create `index.html` - This file will contain the HTML structure necessary for the game's UI.
2. **Task 2**: Create `style.css` - This file will define the CSS styles to make the game visually appealing and responsive.
3. **Task 3**: Create `script.js` - This file will contain the JavaScript code for the game logic and UI interactions.
4. **Code Review Tasks**: Review each file to ensure they meet the project requirements and adhere to the system design.

Let's start by appending the first task to the plan.

```json
[
    {
        "command_name": "Plan.append_task",
        "args": {
            "task_id": "1",
            "dependent_task_ids": [],
            "instruction": "Create the index.html file with the basic HTML structure for the 2048 game.",
            "assignee": "Alex"
        }
    },
    {
        "command_name": "Plan.append_task",
        "args": {
            "task_id": "2",
            "dependent_task_ids": ["1"],
            "instruction": "Create the style.css file with the necessary CSS to style the 2048 game.",
            "assignee": "Alex"
        }
    },
    {
        "command_name": "Plan.append_task",
        "args": {
            "task_id": "3",
            "dependent_task_ids": ["1", "2"],
            "instruction": "Create the script.js file containing the JavaScript logic for the 2048 game.",
            "assignee": "Alex"
        }
    },
    {
        "command_name": "Plan.append_task",
        "args": {
            "task_id": "4",
            "dependent_task_ids": ["1"],
            "instruction": "Use ReviewAndRewriteCode to review the code in index.html to ensure it meets the design specifications.",
            "assignee": "Alex"
        }
    },
    {
        "command_name": "Plan.append_task",
        "args": {
            "task_id": "5",
            "dependent_task_ids": ["2"],
            "instruction": "Use ReviewAndRewriteCode to review the code in style.css to ensure it meets the design specifications.",
            "assignee": "Alex"
        }
    },
    {
        "command_name": "Plan.append_task",
        "args": {
            "task_id": "6",
            "dependent_task_ids": ["3"],
            "instruction": "Use ReviewAndRewriteCode to review the code in script.js to ensure it meets the design specifications.",
            "assignee": "Alex"
        }
    }
]
```
"""

ENGINEER_EXPERIENCES = ((REQ1, RESP1), (REQ2, RESP2))
