#include <bits/stdc++.h>
using namespace std;

/*
 * Каждый участник выходит из бассейна в момент T[k] = swim[1] + ... + swim[k],
 * после чего независимо едет и бежит, финишируя в T[k] + bike[k] + run[k].
 * Итоговое время = max(T[k] + bike[k] + run[k]) по всем k.
 *
 * Оптимальный порядок — сортировка по убыванию (bike + run).
 *
 * Доказательство (обмен соседей):
 * Пусть i стоит перед j и bike[i]+run[i] < bike[j]+run[j].
 * T — момент выхода всех участников до этой пары.
 *
 * До обмена:
 *   finish[i]  = T + swim[i] + bike[i] + run[i]
 *   finish[j]  = T + swim[i] + swim[j] + bike[j] + run[j]
 *
 * После обмена:
 *   finish[j]' = T + swim[j] + bike[j] + run[j]
 *   finish[i]' = T + swim[j] + swim[i] + bike[i] + run[i]
 *
 * Так как bike[i]+run[i] < bike[j]+run[j], то finish[i]' < finish[j],
 * значит максимум после обмена = finish[j]'.
 * А finish[j]' < finish[j] <= max до обмена.
 * Обмен улучшает результат => такой порядок не оптимален => сортируем по убыванию.
 */
 
bool cmp(const vector<long long>& x, const vector<long long>& y) {
    return x[1] + x[2] > y[1] + y[2];
}

long long solve(vector<vector<long long>> a) {
    sort(a.begin(), a.end(), cmp);
    long long t = 0, ans = 0;
    for (auto& x : a) {
        t += x[0];
        ans = max(ans, t + x[1] + x[2]);
    }
    return ans;
}

void tests() {
    cout << solve({{10,5,3},{8,7,4},{6,2,1}}) << "\n"; // 27
    cout << solve({{5,3,2}}) << "\n";                   // 10
    cout << solve({{4,4,4},{4,4,4},{4,4,4}}) << "\n";  // 20
    cout << solve({{1,10,10},{10,1,1}}) << "\n";        // 21
}

int main() {
    tests();

    int n;
    cin >> n;

    vector<vector<long long>> a(n, vector<long long>(3));
    for (auto& x : a)
        cin >> x[0] >> x[1] >> x[2];

    cout << solve(a) << "\n";
}
