# def recursive_sum(n):
#     print(f"-> заходжу в {n}")

#     if n == 1:
#         print(f"<- база {n}")
#         return 1
    
#     result = n + recursive_sum(n - 1)
#     print(f"<- виходжу з {n}, result={result}")
#     return result

# print(recursive_sum(5))

# def filter_words(words):
#     result = []

#     for word in words:
#         if len(word) > 3:
#             result.append(word)
    
#     return result

# words = ['hi', 'cat', 'hello', 'dog', 'python', 'program', 'ide', 'best']
# print(filter_words(words))


#та сама функція за методом list comprehensions
# def filter_words(words):
#     return [word for word in words if len(word) > 3]

# words = ['hi', 'cat', 'hello', 'dog', 'python', 'program', 'ide', 'best']
# print(filter_words(words))


#lambda and filter function
# def filter_words(words):
#     return list(filter(lambda word: len(word) > 3, words))

# words = ['hi', 'cat', 'hello', 'dog', 'python', 'program', 'ide', 'best']

# print(filter_words(words))

# import time


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()

#         result = func(*args, **kwargs)
        
#         end = time.time()
#         print(f"{func.__name__} виконалась за {end - start:.5f}сек")

#         return result
    
#     return wrapper

# @timer
# def slow_function():
#     time.sleep(1)
#     return "done"

# print(slow_function())


