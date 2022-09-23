def common_end(a, b):
    #[0] for beginning [-1] for end
    return a[0] == b[0] or a[-1] == b[-1]

print(common_end([1,2,3,4],[2,3,1,4])) #True
print(common_end([1,2,3,4],[7,5,7,8]))#False