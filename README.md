# aws-sam-cicd

## requirements
- [AWS SAM CLI](https://docs.aws.amazon.com/ko_kr/serverless-application-model/latest/developerguide/prerequisites.html)
- [Docker Desktop](https://docs.aws.amazon.com/ko_kr/serverless-application-model/latest/developerguide/install-docker.html#install-docker-instructions)

## Run
```cmd
git clone https://github.com/jungeun5-choi/aws-sam-cicd.git
cd aws-sam-cicd/
```
```cmd
sam build     # build SAM
sam validate  # validate SAM template
```
```cmd
# local에서 간단하게 api 호출 확인
sam local invoke ApiGatewayFunction -e evnets/event.json
```
```cmd
# local에서 서버 열어서 테스트 가능
sam local start-api
sam local start-api -p ${port}
```
```cmd
# SAM이 변경 감지 → Sync
# = Cloud에 올라간 Stack에서 바로 테스트 가능 > 근
sam sync --stack-name ${stack-name} --watch
sam sync --stack-name sam-stack-prod --watch
```
- `sam sync`는 테스트 계정이나 dev 스택 따로 만들고 그 이름으로 실행하는 걸 권장
- **Stack = CloudFormation Stack**
  - "AWS 리소스들의 묶음(set)"을 정의한 템플릿의 실행 결과
  - 버전 관리되고 추적 가능한 상태로 유지하는 "리소스 집합 단위"
  - 하나의 Stack 안에는 여러 리소스가 있음 (Lambda, API Gateway, S3, IAM Role 등)
  - Stack 단위로 배포, 롤백, 삭제, 업데이트 가능
  - Stack이 실패하면 전체가 롤백됨 (All-or-nothing)
