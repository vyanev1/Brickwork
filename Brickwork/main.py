from layer import BrickLayer


def get_input():
    N, M = [int(num) for num in input().strip().split()]
    if not((N < 100 and M < 100) and (N % 2 == 0 and M % 2 == 0)):
        raise Exception("N and M should be even numbers and define a valid area of less than 100 lines/columns.")
    inputMatrix = []
    for _ in range(N):
        row = [int(num) for num in input().strip().split()]
        if len(row) != M:
            raise Exception("Number of columns on each line should be equal to M")
        inputMatrix.append(row)
    return N, M, inputMatrix


def stringify(arr: list):
    final_str = [['-' for _ in range(len(arr[0]) * 4 + 1)] for _ in range(len(arr) * 2 + 1)]
    for i in range(len(arr)):
        str_i = 1 + i*2
        for j in range(len(arr[i])):
            str_j = 2 + 4*j

            final_str[str_i][str_j - 1] = ' '
            final_str[str_i][str_j] = str(arr[i][j])
            final_str[str_i][str_j + 1] = ' ' if arr[i][j] < 10 else ''

            if j+1 < len(arr[i]) and arr[i][j+1] == arr[i][j]:
                final_str[str_i][str_j + 2] = ' '
            elif i+1 < len(arr) and arr[i+1][j] == arr[i][j]:
                final_str[str_i+1][str_j - 1] = ' '
                final_str[str_i+1][str_j] = ' '
                final_str[str_i+1][str_j + 1] = ' '
    return final_str


if __name__ == '__main__':
    try:
        user_in = get_input()
        N, M, inputMatrix = user_in

        # create a BrickLayer from the input and get the next layer of bricks
        layer = BrickLayer(N, M, inputMatrix)
        next_layer = layer.get_next()

        if next_layer != -1:
            layer_str = stringify(next_layer)
            [print(''.join(row)) for row in layer_str]
        else:
            print(-1)
            print('There is no solution to this input')
    except Exception as e:
        print(e.args[0])
