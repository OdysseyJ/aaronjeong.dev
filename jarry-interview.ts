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


interface Validator {
  validate(): string | undefined
}

class ValidationInput{
  prev = ""
  cur = ""

  constructor(prev: string, cur: string){
    this.prev = prev
    this.cur = cur
  }
}

class AddOverMaximumValidator extends ValidationInput implements Validator{
  validate(): string | undefined {
    if(this.cur.length > 13) return this.prev
  }
}

/*
 * This function is a transformer. Receive prev string to cur string
 * @param prev previous raw string for phone number
 * @param cur changed raw string for phone number
 * @return valid phone number formmated with hyphen pattern e.g.) 010-0000-0000
 * @author you
 * */
export function _______EDIT_________THIS_______ONLY__________(
    prev: string,
    cur: string,
): string {
  const isAddition = cur.length === prev.length + 1
  const isDeletion = cur.length === prev.length - 1
  const isCopying = cur.length > prev.length && cur.length - prev.length >= 2
  const isCutting = cur.length < prev.length && prev.length - cur.length >= 2

  let validatorClasses : typeof AddOverMaximumValidator[] = []
  if (isAddition) {
    validatorClasses.push(AddOverMaximumValidator)
  }
  if (isDeletion) {
    validatorClasses.push(AddOverMaximumValidator)
  }
  if (isCopying){
    validatorClasses.push(AddOverMaximumValidator)
  }
  if (isCutting){
    validatorClasses.push(AddOverMaximumValidator)
  }
  validatorClasses.forEach((validatorClass)=>{
    const result = new validatorClass(prev, cur).validate()
    if (result) return result
  })
  return '';
}
