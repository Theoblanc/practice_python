def recursive_test(cnt):
    cnt = cnt + 1
    if cnt < 10:
        recursive_test(cnt)
        print(cnt)
    else:
        return cnt


recursive_test(0)


#
# recursive_test(0)
#   recursive_test(1)
#       recursive_test(2)
