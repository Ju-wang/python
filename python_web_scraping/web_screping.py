from indeed import get_jobs as get_indeed_jobs
from stack_over_flow import get_jobs as get_so_jobs
from save import save_to_file


indeed_jobs = get_indeed_jobs()  # 최종 결과물은 jobs 리스트이다
so_jobs = get_so_jobs()  # 최종 결과물은 jobs 리스트이다
jobs = so_jobs + indeed_jobs

save_to_file(jobs)
