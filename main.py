#!/usr/bin/env python3
import json
import os
import sys

STORAGE = "storage.json"

def load_todos():
    if not os.path.exists(STORAGE):
        return []
    with open(STORAGE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_todos(todos):
    with open(STORAGE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2, ensure_ascii=False)

def list_todos():
    todos = load_todos()
    if not todos:
        print("مفيش مهام لحد دلوقتي.")
        return
    for i, t in enumerate(todos, 1):
        status = "[x]" if t.get("done") else "[ ]"
        print(f"{i}. {status} {t.get('task')}")

def add_todo(task):
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print("تمت الإضافة ✅")

def mark_done(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["done"] = True
        save_todos(todos)
        print("اتعملت علامة إن المهمة خلصت ✅")
    else:
        print("رقم المهمة مش صحيح.")

def remove_todo(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        save_todos(todos)
        print(f"تم حذف: {removed.get('task')}")
    else:
        print("رقم المهمة مش صحيح.")

def clear_todos():
    save_todos([])
    print("تم مسح كل المهام.")

def help_msg():
    print("""Usage:
    todo add "task description"    - إضافة مهمة
    todo list                      - عرض كل المهام
    todo done <number>             - تعليم مهمة كمكتملة
    todo remove <number>           - حذف مهمة
    todo clear                     - مسح كل المهام
    todo help                      - عرض المساعدة
    """)

def main():
    if len(sys.argv) < 2:
        help_msg()
        return
    cmd = sys.argv[1].lower()
    if cmd == "add":
        if len(sys.argv) < 3:
            print("اكتب وصف المهمة بين علامات اقتباس.")
            return
        task = " ".join(sys.argv[2:])
        add_todo(task)
    elif cmd == "list":
        list_todos()
    elif cmd == "done":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("اكتب رقم المهمة اللي هتعلّمه كمكتملة.")
            return
        mark_done(int(sys.argv[2]) - 1)
    elif cmd == "remove":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("اكتب رقم المهمة اللي عايز تحذفها.")
            return
        remove_todo(int(sys.argv[2]) - 1)
    elif cmd == "clear":
        clear_todos()
    else:
        help_msg()

if __name__ == "__main__":
    main()
