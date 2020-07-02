def array_test():
    arr = [3, 2, 5, 6]

    arr.pop()

    print("array pop :", arr)

    arr.append(7)
    print("array push: ", arr)

    # 위치 찾기(index 반환)
    print("index : ", arr.index(2))

    arr.reverse()

    print("reverse :", arr)

    print(sorted(arr))

    print('__name__:', __name__)    # __name__ 변수 출력


def main():
    array_test()


if __name__ == "__main__":
    main()
