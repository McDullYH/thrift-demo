namespace py printer

enum Usage {
    PACK = 1,
    UNPACK =2
}

exception InvalidOperation {
    1:i32 id,
    2:string describe
}

struct Box {
    1: i32 id,
    2: double weight,
    3: string name,
    4: Usage useage,
    5: optional string describe,
}

service PrinterService {
    bool printBool(1:bool boolValue),
    map<i32,string> printMap(1:map<i32,string> mapValue),
    Box printBox(1:Box box) throws (1:InvalidOperation inOp),
    oneway void verbose(1:string cmd)
}
