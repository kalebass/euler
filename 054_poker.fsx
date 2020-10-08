open System
open System.IO

type Suit =
    | Hearts
    | Clubs
    | Diamonds
    | Spades
type Rank = int
type Card = { Rank: Rank; Suit: Suit }
type Hand =
    | HighCard
    | Pair
    | TwoPair
    | ThreeOfAKind
    | Straight
    | Flush
    | FullHouse
    | FourOfAKind
    | StraightFlush

let card (code: string) =
    let rank =
        match Char.ToUpper(code.[0]) with
        | 'A' -> 14
        | 'K' -> 13
        | 'Q' -> 12
        | 'J' -> 11
        | 'T' -> 10
        | ch when Char.IsDigit(ch) -> int ch - int '0'
        | _ -> failwith "Wrong rank code"
    let suit =
        match Char.ToUpper(code.[1]) with
        | 'H' -> Suit.Hearts
        | 'D' -> Suit.Diamonds
        | 'C' -> Suit.Clubs
        | 'S' -> Suit.Spades
        | _ -> failwith "Wrong suit code"
    { Suit = suit; Rank = rank }

let cardsFromString (str: string) =
    str.Split() |> Seq.map card |> Seq.toList

let handType cards =
    let rankCounts =
        cards
        |> List.countBy (fun card -> card.Rank)
        |> List.map snd

    match List.max rankCounts with
    | 4 -> FourOfAKind
    | 3 ->
        if List.contains 2 rankCounts then FullHouse else ThreeOfAKind
    | 2 ->
        if List.length rankCounts = 3 then TwoPair else Pair
    | _ ->
        let flush =
            cards
            |> List.countBy (fun card -> card.Suit)
            |> List.length = 1
        let straight =
            let ranks = cards |> List.map (fun card -> card.Rank)
            List.max ranks - List.min ranks = 4
            || List.sort ranks = [2; 3; 4; 5; 14]
        if straight && flush then
            StraightFlush
        elif flush then
            Flush
        elif straight then
            Straight
        else
            HighCard

let player1Wins handPair =
    let cards = cardsFromString handPair
    let cards1 = cards.[..4]
    let cards2 = cards.[5..]
    let hand1 = handType cards1
    let hand2 = handType cards2
    if hand1 <> hand2 then
        hand1 > hand2
    else
        let ranks1 =
            cards1
            |> List.countBy (fun card -> card.Rank)
            |> List.sortByDescending fst
            |> List.sortByDescending snd
            |> List.map fst
        let ranks2 =
            cards2
            |> List.countBy (fun card -> card.Rank)
            |> List.sortByDescending fst
            |> List.sortByDescending snd
            |> List.map fst
        Seq.compareWith (fun r1 r2 -> r1 - r2) ranks1 ranks2 > 0

let readLines fileName = seq {
    use sr = new StreamReader(fileName: string)
    while not sr.EndOfStream do
        yield sr.ReadLine()
}

let res =
    readLines "F:\Development\Project Euler\p054_poker.txt"
    |> Seq.filter player1Wins
    |> Seq.length
