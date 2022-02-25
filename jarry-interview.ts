export {}
// 난이도 하
// 해당 함수의 리턴 타입은?
// const sendSlackMessage = async (message: string) => {
//   const isSucceed: boolean = await callSlackApi()
//   return { isSucceed }
// }

// 난이도 중
// 현재 Slack 서버가 불안정해서 위의 sendSlackMessage를 1000번 실행한 다음,
// 1000번의 실행중 몇번이 성공했는지 보고 싶습니다.
// const howManySucceed = async () => {
//   let succeed = 0
//   // 구현
//   return succeed
// }

// 난이도 상
// 해당 코드가 갖는 문제점을 클린코드 관점에서 설명해보기, 리팩토링
// 힌트 : 함수의 책임, 조건 분기, 클래스 다형성
// class Airplane {
//   // ...
//   getCruisingAltitude() {
//     switch (this.type) {
//       case 'Boeing777':
//         return this.getMaxAltitude() - this.getPassengerCount();
//       case 'Air Force One':
//         return this.getMaxAltitude();
//       case 'Cessna':
//         return this.getMaxAltitude() - this.getFuelExpenditure();
//     }
//   }
// }