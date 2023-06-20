# # O(N**2)
# def str_counter(s):
#     for sym in set(s):
#         count = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 count += 1
#         print(f'{sym} - {count}')
#
#
# str_counter("abc")
#
# for i in range(1, 11):
#     for f in range(1, 11):
#         print(i, f)


# O(N)
def better_str_counter(s):
    for sym in set(s):
        print(f'{sym} - {s.count(sym)}')


better_str_counter('avvvsghhe')
