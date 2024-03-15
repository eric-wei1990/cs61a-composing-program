function make_withdraw(balance) {
    function withdraw(amount) {
        if (amount > balance) {
            return 'Insufficient balance';
        }

        balance = balance - amount;

        return balance;
    }

    return withdraw;
}

const wd = make_withdraw(100);

console.log(wd(5));
console.log(wd(3));