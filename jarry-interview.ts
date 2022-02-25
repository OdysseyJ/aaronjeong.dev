// Typescript
// 해당 함수의 리턴 타입은 뭔가요?
const sendSlackMessage = async (message: str)=>{
  await callSlackApi()
  return { isSucceed: true }
}

// Javascript Clean Code
// 아래와 같은 클래스에 getCruisingAltitude함수가 있어요.
// 해당 코드가 갖는 문제점을 클린코드 관점에서 설명해보실 수 있나요?
// 힌트 : 1. 함수의 책임, 2. 조건 분기
class Airplane {
  // ...
  getCruisingAltitude() {
    switch (this.type) {
      case 'Boeing777':
        return this.getMaxAltitude() - this.getPassengerCount();
      case 'Air Force One':
        return this.getMaxAltitude();
      case 'Cessna':
        return this.getMaxAltitude() - this.getFuelExpenditure();
    }
  }
}

// 제리가 이전에 만드신 Airplane 클래스를
// 이미 다른 사람들이 100군데가 넘는 곳에서 해당 형식으로 코드를 사용하고 있었어요.
const airplanes : Airplane[] = []
airplanes.forEach((airplane)=>{
  const cruisingAltitude = airplane.getCruisingAltitude()
  //...
})
// 다른 사람들에게 100곳의 코드를 고쳐달라고 부탁하지 않고, 제리가 작성한 코드를 리팩토링하려면 어떻게 해야할까요?
// 힌트 : 클래스와 다형성










// 정답 :
class Airplane {
  // ...
}

class Boeing777 extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude() - this.getPassengerCount();
  }
}

class AirForceOne extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude();
  }
}

class Cessna extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude() - this.getFuelExpenditure();
  }
}