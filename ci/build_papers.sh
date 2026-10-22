#!/usr/bin/env bash
#
#   Build and check the given paper directories (PIDs), e.g.
#       ci/build_papers.sh C101 P203
#   With no arguments every papers/*/ directory is built.
#
#   A LaTeX failure fails the script; PaperCheck problems are only reported,
#   since they are for the editors to judge in the PR review.

cd "$(dirname "$0")/.."

pids=("$@")
if [ ${#pids[@]} -eq 0 ]; then
    pids=($(ls papers))
fi

summary=${GITHUB_STEP_SUMMARY:-/dev/null}
echo "| Paper | LaTeX | PaperCheck |" >> "$summary"
echo "|---|---|---|"                  >> "$summary"

status=0
for pid in "${pids[@]}"; do
    dir=papers/$pid
    if [ ! -f "$dir/makedefs" ]; then
        echo "::warning::$dir has no makedefs, skipping"
        continue
    fi

    echo "::group::$pid: make pdf"
    (cd "$dir" && make clean > /dev/null && make pdf < /dev/null)
    built=$?
    echo "::endgroup::"
    if [ $built -eq 0 ]; then
        latex="built"
    else
        latex="**FAILED**"
        status=1
        echo "::error file=$dir/$pid.tex::LaTeX build failed for $pid"
        # the TeX errors themselves, which start with "!"
        [ -f "$dir/$pid.log" ] && grep -n -A4 '^!' "$dir/$pid.log"
    fi

    echo "::group::$pid: make check"
    (cd "$dir" && make check)
    checked=$?
    echo "::endgroup::"
    if [ $checked -eq 0 ]; then
        check="ok"
    else
        check="problems (see log)"
        echo "::warning file=$dir/$pid.tex::PaperCheck reported problems for $pid"
    fi

    echo "| $pid | $latex | $check |" >> "$summary"
done

exit $status
