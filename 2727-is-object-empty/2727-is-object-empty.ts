type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | JSONValue[]

function isEmpty(obj: Obj): boolean {
    let content = JSON.stringify(obj)
    return content.length <= 2 ? true : false
};