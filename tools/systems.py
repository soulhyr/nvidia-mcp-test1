# tools/system.py
import os
import shutil
from mcp.server.fastmcp import FastMCP

def register_system_tools(mcp: FastMCP):
    @mcp.tool()
    async def reset_data() -> str:
        """모든 데이터(직원 정보, 할 일)를 초기화합니다."""
        data_paths = ["data/employees", "data/todos", "data/todo_list.json"]
        
        results = []
        for path in data_paths:
            if os.path.exists(path):
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    results.append(f"폴더 삭제: {path}")
                else:
                    os.remove(path)
                    results.append(f"파일 삭제: {path}")
        
        # 필수 폴더 다시 생성
        os.makedirs("data/employees", exist_ok=True)
        os.makedirs("data/todos", exist_ok=True)
        
        return "데이터 초기화 완료: " + ", ".join(results)