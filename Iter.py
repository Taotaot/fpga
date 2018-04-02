＃！/ usr / bin / env python3
＃ -  *  - 编码：utf-8  -  *  -

从集合中导入 Iterable，Iterator

def  g（）：
    产量 1
    产量 2
    产量 3

打印（'可迭代[1，2，3]：'，isinstance（[ 1，2，3 ]，可迭代））
print（' Iterable？\' abc \'：'，isinstance（' abc '，Iterable））
print（' Iterable？123：'，isinstance（123，Iterable））
print（' Iterable？g（）：'，isinstance（g（），Iterable））

打印（'迭代[1，2，3]：'，isinstance（[ 1，2，3 ]，迭代器））
打印（'？迭代器ITER（[1，2，3]）：'，isinstance（ITER（[ 1，2，3 ]），迭代器））
print（' Iterator？\' abc \'：'，isinstance（' abc '，Iterator））
print（' Iterator？123：'，isinstance（123，Iterator））
print（' Iterator？g（）：'，isinstance（g（），Iterator））

＃ ITER列表：
print（' for [in [1，2，3，4，5]：'）
对于 X 在 [ 1，2，3，4，5 ]：
    打印（x）

print（' for x in iter（[1，2，3，4，5]）：'）
对于 X 在 ITER（[ 1，2，3，4，5 ]）：
    打印（x）

print（' next（）：'）
它=  ITER（[ 1，2，3，4，5 ]）
打印（下一个（it））
打印（下一个（it））
打印（下一个（it））
打印（下一个（it））
打印（下一个（it））

d = { ' a '：1，' b '：2，' c '：3 }

＃ ITER每个键：
打印（' iter key：'，d）
用于 ķ 在运行起来也（）：
    打印（' key：'，k）

＃ ITER每个值：
打印（' iter value：'，d）
for v in d.values（）：
    print（' value：'，v）

＃ ITER两个键和值：
打印（' iter item：'，d）
for k，v in d.items（）：
    print（' item：'，k，v）

＃索引列表：
print（' iter enumerate（[ \' A \'，\' B \'，\' C \' ] '）
对于 I，值在 枚举（[ '甲'，'乙'，' Ç ' ]）：
    打印（我，价值）

＃ ITER复杂的列表：
print（' iter [（1，1），（2，4），（3，9）]：'）
为 X，Y 在 [（1，1），（2，4），（3，9）]：
    print（x，y）
