let digitSquareSum (n : int) =
    string n
    |> Seq.map (fun character -> int character - 48)
    |> Seq.map (fun digit -> digit*digit)
    |> Seq.sum

let cache = Array.create 600 (None : bool option)
cache.[1] <- Some(true)
cache.[89] <- Some(false)

let endsAtOne n =
    let rec tailEndsAtOne n tocache =
        if n < 600 && Option.isSome cache.[n] then
            let result = cache.[n]
            for n in tocache do
                if n < 600 then
                    cache.[n] <- result
            Option.get result
        else
            tailEndsAtOne (digitSquareSum n) (n :: tocache)
    tailEndsAtOne n []


//let rec endsAtOne n =
//    match n with
//    | 1 -> true
//    | 89 -> false
//    | n -> endsAtOne (digitSquareSum n)

#time

let result =
    seq { 1 .. 10000000 }
    |> Seq.where endsAtOne
    |> Seq.length

#time
