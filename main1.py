
def calculate_balance(balance, amount, operation):
    if operation == "deposit":
        return balance + amount
    elif operation == "withdraw":
        if amount > balance:
            return "余额不足"
        return balance - amount
    else:
        return "不支持的操作"


if __name__ == "__main__":
    balance = 1000

    print("初始余额：", balance)

    balance = calculate_balance(balance, 500, "deposit")
    print("存款后余额：", balance)

    balance = calculate_balance(balance, 200, "withdraw")
    print("取款后余额：", balance)
    print("Git 第二次提交练习完成！")