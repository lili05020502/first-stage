console.log("--Task1--")

function findAndPrint(messages) {
    // write down your judgment rules in comments
    // your code here, based on your own rules
    Object.entries(messages).forEach(item => {
        // debugger;
        if (item[1].search(/18 years old/i) >= 0) console.log(item[0]);
        if (item[1].search(/college student/i) >= 0) console.log(item[0]);
        if (item[1].search(/legal age/i) >= 0) console.log(item[0]);
        if (item[1].search(/I will vote/i) >= 0) console.log(item[0]);
    });
}
findAndPrint({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
});

console.log("--Task2--")

function calculateSumOfBonus(data){
    // write down your bonus rule in comments
    // your code here, based on your own rules
    let totalbonus =0;
    data.employees.forEach(item => {
        // debugger;
        let bonus =0;
        // console.log(item);
        if (typeof (item.salary) == "number") { item.salary = item.salary.toString(); };
        // console.log(item.salary,typeof item.salary);
        if (item.salary.search(/USD/g) >= 0) { item.salary = item.salary.replace("USD", "") * 30; };
        // console.log(item.salary,typeof item.salary);
        if (typeof (item.salary) == "number") { item.salary = item.salary.toString(); };
        // console.log(item.salary,typeof item.salary);
        if (item.salary.search(/,/g) >= 0) {item.salary = item.salary.replace(",", "");};
        // console.log(item.salary,typeof item.salary);
        // console.log(item)
        if(item.performance =="above average"){bonus = item.salary*0.09;};
        // console.log("bonus"+bonus);
        if(item.performance =="average"){bonus = item.salary*0.07;};
        // console.log("bonus"+bonus);
        if(item.performance =="below average"){bonus = item.salary*0.03;};
        // console.log("bonus"+bonus);
        if(item.role =="Engineer"){bonus=bonus*0.8;};
        if(item.role =="CEO"){bonus=bonus*0.9;};
        if(item.role =="Sales"){bonus=bonus*0.7;};
        // console.log(item.name+" bonus:"+bonus);

        totalbonus+=bonus;
        
    });
    console.log("Total Bonus:"+Math.round(totalbonus)+ " TWD");

}
calculateSumOfBonus({
    "employees":[
    {
    "name":"John",
    "salary":"1000USD",
    "performance":"above average",
    "role":"Engineer"
    },
    {
    "name":"Bob",
    "salary":60000,
    "performance":"average",
    "role":"CEO"
    },
    {
    "name":"Jenny",
    "salary":"50,000",
    "performance":"below average",
    "role":"Sales"
    }
    ]
    }); // call calculateSumOfBonus function


    console.log("--Task3--")

    function func(...data){
        // your code here
        // debugger
    
        let Output = false;
        for (i = 0; i < data.length; i++) {
            let flag = true;
    
            for (j = 0; j < data.length; j++) {
                if (i != j) {
                    if (data[i][1] == data[j][1]) {
                        flag = false;
    
                    }
                }
            }
            // (flag)  ? console.log(data[i]) : console.log("沒有");
            if (flag) { console.log(data[i]); Output = true; }
        } if (Output == false) { console.log("沒有"); }
    }
    func("彭⼤牆", "王明雅", "吳明"); // print 彭⼤牆
    func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
    func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有


console.log("--Task4--")

function getNumber(index){
    // your code here
    looplen =Math.floor(index/2) + (index %2)
    let list = [0];
    let last = 0;
    for (let i = 0; i < looplen; i++) { 
        last+=3;
        list.push(last+1);
        list.push(last)

    }
return console.log(list[index]);
}
getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15


