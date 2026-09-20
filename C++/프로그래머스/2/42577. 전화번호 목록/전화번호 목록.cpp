#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    // 1. 전화번호 목록을 사전순으로 정렬
    sort(phone_book.begin(), phone_book.end());
    
    // 2. 인접한 두 번호를 비교하여 앞 번호가 뒷 번호의 접두사인지 확인
    for (size_t i = 0; i < phone_book.size() - 1; ++i) {
        if (phone_book[i + 1].rfind(phone_book[i], 0) == 0) {
            return false; // 접두사인 경우 false 반환
        }
    }
    
    return true; // 접두사인 경우가 없으면 true 반환
}