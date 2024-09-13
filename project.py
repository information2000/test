# todo.py

# 간단한 To-Do List 프로그램
todo_list = []

def show_todos():
    print("\n현재 To-Do 목록:")
    if not todo_list:
        print("할 일이 없습니다.")
    else:
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")
    print()

def add_todo():
    task = input("추가할 할 일을 입력하세요: ")
    todo_list.append(task)
    print(f"할 일 '{task}'가 추가되었습니다.\n")

def remove_todo():
    show_todos()
    try:
        task_number = int(input("삭제할 할 일 번호를 입력하세요: "))
        if 0 < task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"할 일 '{removed_task}'가 삭제되었습니다.\n")
        else:
            print("잘못된 번호입니다. 다시 시도하세요.\n")
    except ValueError:
        print("번호를 입력해 주세요.\n")

def main():
    print("간단한 To-Do List 프로그램에 오신 것을 환영합니다!")
    
    while True:
        print("옵션: add - 할 일 추가, show - 할 일 표시, remove - 할 일 삭제, exit - 종료")
        choice = input("옵션을 선택하세요: ").strip().lower()

        if choice == "add":
            add_todo()
        elif choice == "show":
            show_todos()
        elif choice == "remove":
            remove_todo()
        elif choice == "exit":
            print("프로그램을 종료합니다. 감사합니다!")
            break
        else:
            print("잘못된 옵션입니다. 다시 선택하세요.\n")

if __name__ == "__main__":
    main()

print("freshman")
