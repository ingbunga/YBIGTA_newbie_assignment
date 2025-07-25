
# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
## TODO
if ! which conda &> /dev/null; then
    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm ~/miniconda3/miniconda.sh

    source ~/miniconda3/bin/activate
fi

# Conda 환셩 생성 및 활성화
## TODO
source "$(conda info --base)/etc/profile.d/conda.sh"
conda create --name myenv python==3.11 -y
conda init
conda activate myenv 


## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
## TODO
python3 -m pip install mypy


# Submission 폴더 파일 실행
cd submission || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    ## TODO
    filename=${file%.py}
    cat "../input/${filename}_input" | python3 $file > "../output/${filename}_output"
done

# mypy 테스트 실행 및 mypy_log.txt 저장
## TODO
mypy . > ../mypy_log.txt

# conda.yml 파일 생성
## TODO
conda env export > ../conda.yml

# 가상환경 비활성화
## TODO
conda deactivate