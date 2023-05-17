declare -a my_array=(
"element1"
"element2"
"element3"
"element4"
"element5"
)

for element in "${my_array[@]}"
do
  echo "$element"
done
