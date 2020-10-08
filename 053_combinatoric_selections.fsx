let factorial x =
    let rec tailRecursiveFactorial x acc =
        if x <= 1I then
            acc
        else
            tailRecursiveFactorial (x - 1I) (acc * x)
    tailRecursiveFactorial x 1I

let combinations n k =
    (factorial n) / ((factorial k) * factorial (n - k))

let n_max = 100I
let value_min = 1000001I

let values =
    seq {
        for n in 0I .. n_max do
            for k in 0I .. n do
                yield combinations n k
    }

let result =
    values
    |> Seq.where (fun x -> (x >= value_min))
    |> Seq.length
