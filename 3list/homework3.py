davlatlar=["germaniya","avstraliya","buyuk britaniya","saudiya arabistoni","o'zbekiston"]
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# print(davlatlar)
davlatlar.reverse()
# print(davlatlar)
davlatlar.sort()
# print(davlatlar)
davlatlar.sort(reverse=True)
# print(davlatlar)
a=range(120,1200,2)
# print(3list(a))
# print(sum(3list(a)))
b=max(a)
c=min(a)
# print(b-c)
# print(len(a))
# print(3list(a[:20]))
# print(3list(a[-20:]))
# print(3list(a[510:550]))

taomlar=["palov","manti","yimirta barak","lag'mon","go'mma"]
nonushta=taomlar[-3:]
nonushta.reverse()
del nonushta[1]
nonushta.append("murabbo")
nonushta.append("sariyog'")
nonushta = taomlar
nonushta=tuple(nonushta)
print(nonushta)
print(taomlar)
