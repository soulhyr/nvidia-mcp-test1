import os

def register_policy_resources(mcp):
    POLICY_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "policy", "company_policy_2026.md")

    def read_policy_file():
        if os.path.exists(POLICY_PATH):
            with open(POLICY_PATH, "r", encoding="utf-8") as f:
                return f.read()
        return "규정 파일을 찾을 수 없습니다."

    # 1. 전체 문서 리소스
    @mcp.resource("policy://full")
    def get_full_policy() -> str:
        """사내 규정 문서 전체 내용을 반환합니다."""
        return read_policy_file()

    # 2. 키워드 검색 리소스 템플릿
    @mcp.resource("policy://search/{keyword}")
    def search_policy(keyword: str) -> str:
        """특정 키워드로 규정을 검색하여 필터링된 내용을 반환합니다."""
        content = read_policy_file()
        lines = [line for line in content.split('\n') if keyword.lower() in line.lower()]
        return "\n".join(lines) if lines else "검색 결과가 없습니다."