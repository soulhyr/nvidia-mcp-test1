import os
import asyncio

def search_alarm_tools(mcp):
    DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "employees")
    os.makedirs(DATA_DIR, exist_ok=True)

    @mcp.tool()
    async def set_timer(seconds: int, message: str = "타이머가 종료되었습니다!") -> str:
        """지정한 시간(초)이 지난 후 백그라운드에서 알림 메시지를 출력합니다.

        Args:
            seconds: 타이머 시간 (초 단위, 예: 10분 = 600)
            message: 타이머가 끝났을 때 출력할 알림 메시지
        """
        # 백그라운드로 실행할 비동기 함수 정의
        async def run_timer():
            await asyncio.sleep(seconds)
            # 실제 환경에서는 스피커 음성 출력, Windows 알림, Discord 메시지 등으로 대체
            print(f"\n⏰ [타이머 알림]: {message}")

        # 타이머를 백그라운드 작업(Task)으로 등록 (LLM과 유저는 기다리지 않고 즉시 응답받음)
        asyncio.create_task(run_timer())

        minutes = seconds // 60
        rem_seconds = seconds % 60
        time_str = f"{minutes}분 {rem_seconds}초" if minutes > 0 else f"{seconds}초"

        return f"⏱️ {time_str} 뒤에 '{message}' 알림을 받도록 타이머를 설정했습니다."