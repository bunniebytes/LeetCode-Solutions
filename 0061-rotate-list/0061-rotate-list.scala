object Solution:
    def rotateRight(head: ListNode, _k: Int): ListNode =
        var k = _k
        if k < 1 || head == null || head.next == null then
            head
        else
            var totalLen = 0
            var nthToLast: ListNode = null
            var last: ListNode = null

            def recur(node: ListNode): Int =
                if node == null then
                    k = k % totalLen
                    0
                else
                    totalLen += 1
                    if node.next == null then
                        last = node
                    val thisNum = 1 + recur(node.next)
                    if thisNum == k + 1 then
                        node.next = null
                    if thisNum == k then
                        nthToLast = node
                    thisNum
            recur(head)

            if k == 0 then
                head
            else
                last.next = head
                nthToLast
