import numpy as np
import matplotlib.pyplot as plt
f = np.array([
2704899,3105421,1705109,3149538,1899785,2192683,2986978,1827716,3083510,1813893,
2296806,3035596,2866723,1701996,2832348,2978316,2094881,2598303,2279577,1890624,
2689544,2468717,2914777,2833078,2203512,1337041,2106024,2027347,1118162,1700049,
2400749,1560946,2575401,1859169,1442183,1821173,2059865,1989162,1639846,1878229,
1700540,2408338,2044065,2190356,1658232,2249649,2872648,1894235,1056160,1413513,
1883692,3021141,2063239,1715627,1995966,1501497,2836282,1311121,1473949,2490962,
1329035,1737860,1854468,1943841,2408563,2525583,2008769,2380085,2365929,2172743,
1697608,1064570,2465552,2424480,2236322,1273686,2184465,2964330,3447166,2707678,
2787777,1639881,1908933,1556879,1490701,1883312,1596099,2463142,1596736,2491106,
2507554,2908217,1959082,2076743,1841910,1592335, 894755,1972020,1296720,1917613,
2055741,1859322,2545406,2501931,2047398,3521671,1257761,1684747,2805866,2292377,
2101271,2162486,1528744,2498397], dtype=float)

N = len(f)                   
assert N == 114
t = np.arange(1, N + 1)      
w0 = 2 * np.pi / N           

# (a)  
K = N // 2                      # Nyquist: k = 0..57
Re = np.zeros(K + 1); Im = np.zeros(K + 1)
for k in range(K + 1):
    s_c = 0.0; s_s = 0.0
    for tt in range(N):
        s_c += f[tt] * np.cos(k * w0 * t[tt])
        s_s += f[tt] * np.sin(k * w0 * t[tt])
    Re[k] = s_c; Im[k] = -s_s   # F_k = Re + i Im
a = 2 * Re / N;  b = -2 * Im / N
a[0] = Re[0] / N                
a[K] = Re[K] / N; b[K] = 0.0    
freq = np.arange(K + 1) / N     
power = (Re**2 + Im**2) / N     
print(f"a0 (mean flow) = {a[0]:.2f} ac-ft/yr\n")
print(" k   freq(1/yr)  period(yr)        a_k            b_k            Power")
for k in range(K + 1):
    per = N / k if k else np.inf
    print(f"{k:2d}  {freq[k]:9.5f}  {per:9.2f}  {a[k]:14.2f} {b[k]:14.2f}  {power[k]:14.5e}")

# (c)
idx = np.argsort(power[1:])[::-1][:3] + 1
print("\nThree most dominant frequencies:")
for r, k in enumerate(idx, 1):
    print(f"  {r}. k = {k:2d}, f = {freq[k]:.5f} cycles/yr, period = {N/k:.2f} yr, power = {power[k]:.4e}")
# (b) 
plt.figure(figsize=(9, 5))
plt.stem(freq[1:], power[1:], basefmt=' ')
for k in idx:
    plt.annotate(f"f={freq[k]:.4f}\n(T≈{N/k:.1f} yr)", (freq[k], power[k]),
                 textcoords='offset points', xytext=(5, 5), fontsize=8, color='red')
plt.xlabel('Frequency (cycles/year)'); plt.ylabel('Power  |F_k|² / N')
plt.title('Power spectrum of annual river flow (1906–2019)')
plt.grid(alpha=0.3); plt.tight_layout(); plt.savefig('q2_power_spectrum.png', dpi=200)
print("\nPlot saved: q2_power_spectrum.png")