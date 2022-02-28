export {}
// 난이도 하
// 1. 해당 함수의 리턴 타입은?
const sendSlackMessage = async (message: string) => {
  const isSucceed: boolean = await callSlackApi()
  return { isSucceed }
}

// 2. useEffect의 동작방식에 대해서 설명해달라.

// 난이도 중
// 3. 현재 Slack 서버가 불안정해서 위의 sendSlackMessage를 1000번 실행한 다음,
// 1000번의 실행중 몇번이 성공했는지 보고 싶습니다.
const howManySucceed = async () => {
  let succeed = 0
  // 구현
  return succeed
}

// 난이도 상
// 4. 해당 코드가 갖는 문제점을 클린코드 관점에서 설명해보기, 리팩토링
// 힌트 : 함수의 책임, 조건 분기, 클래스 다형성
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


interface ValidatorInterface {
  validate(): string | undefined
}

class NormalizedValidationInput{
  prev = ""
  cur = ""

  constructor(prev: string, cur: string){
    this.prev = this._normalize(prev)
    this.cur = this._normalize(cur)
  }

  _normalize(text: string){
    return text
  }
}

class Validatior extends NormalizedValidationInput implements ValidatorInterface{
  validate(): string | undefined {
    return
  }
}

class AddOverMaximumValidator extends Validatior{
  validate(): string | undefined {
    if(this.cur.length > 13) return this.prev
  }
}

class AddNoNeedChangeValidator extends Validatior {
  validate(): string | undefined {
    if (this.prev.length === 13) return this.prev
  }
}

export function _______EDIT_________THIS_______ONLY__________(
    prev: string,
    cur: string,
): string {
  const isAddition = cur.length === prev.length + 1
  const isDeletion = cur.length === prev.length - 1
  const isCopying = cur.length > prev.length && cur.length - prev.length >= 2
  const isCutting = cur.length < prev.length && prev.length - cur.length >= 2

  let validatorClasses : typeof Validatior[] = []
  if (isAddition) {
    validatorClasses.push(AddNoNeedChangeValidator)
    validatorClasses.push(AddOverMaximumValidator)
  }
  if (isDeletion) {
    // ...
  }
  if (isCopying){
    // ...
  }
  if (isCutting){
    // ...
  }
  validatorClasses.forEach((validatorClass)=>{
    const result = new validatorClass(prev, cur).validate()
    if (result) return result
  })
  return cur;
}

