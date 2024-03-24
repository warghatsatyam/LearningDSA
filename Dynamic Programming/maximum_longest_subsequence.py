

# def longest_subsequence(i,j,str1,str2,dp):
#     if i>=len(str1) or j>=len(str2):
#         dp[i][j]=0
#         return 0
#     if i==len(str1)-1 and j==len(str2)-1 and str1[i]==str2[j]:
#         dp[i][j]= 1
#         return 1 
#     if i==len(str1)-1 and j==len(str2)-1 and str1[i]!=str2[j]:
#         dp[i][j] = 0
#         return 0 
#     if str1[i] == str2[j] and dp[i][j]==-1:
#         dp[i][j] =1 + longest_subsequence(i+1,j+1,str1,str2,dp)
#         return dp[i][j]
#     if str1[i] == str2[j] and dp[i][j]!=-1:
#         return dp[i][j]
    
#     if str1[i]!=str2[j]:
#         if dp[i][j+1]==-1:
#             ans1 = longest_subsequence(i,j+1,str1,str2,dp)
#             dp[i][j+1] = ans1
#         else:
#             ans1 = dp[i][j+1]

#         if dp[i+1][j]==-1:
#             ans2 = longest_subsequence(i+1,j,str1,str2,dp)
#             dp[i+1][j] = ans2
#         else:
#             ans2 = dp[i+1][j]
#         return max(ans1,ans2)
    
# if __name__ == '__main__':
#     str1 = 'abdgec'
#     str2 = 'bfdmgjc'
#     dp = [[ -1 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
#     ans = longest_subsequence(0,0,str1,str2,dp)
#     print(ans)



from sys import stdin

def lcs(s, t,i,j,dp) :
	#Your code goes here
	if i>=len(s) or j>=len(t):
		dp[i][j]=0
		return 0 
	if i==len(s)-1 and j==len(t)-1 and s[i]==t[j]:
		dp[i][j]=1
		return 1
	if i==len(s)-1 and j == len(t)-1 and s[i]!=t[j]:
		dp[i][j]=0
		return 0
	if s[i] == t[j] and dp[i][j] == -1:
		dp[i][j] = 1 + lcs(s,t,i+1,j+1,dp)
		return dp[i][j]
	if s[i] == t[j] and dp[i][j] == -1:
		return dp[i][j]

	if s[i]!=t[j]:
		if dp[i][j+1] == -1:
			ans1 = lcs(s,t,i,j+1,dp)
			dp[i][j+1] = ans1
		else:
			ans1 = dp[i][j+1]

		if dp[i+1][j] == -1:
			ans2 = lcs(s,t,i+1,j,dp)
			dp[i+1][j] = ans2 
		else:
			ans2 = dp[i+1][j]

		return max(ans1,ans2)


#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

dp = [[ -1 for j in range(len(t)+1)] for i in range(len(s)+1)]
print(lcs(s, t,0,0,dp))