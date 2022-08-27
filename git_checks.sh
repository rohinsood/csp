echo "Check if user is properly signed into git"

cd ~

declare -A settings=(["name"]="" ["email"]="")

echo -n "Enter your GitHub username: "
read settings["name"]

echo -n "Enter the email you use with GitHub: "
read settings["email"]

printf "\n"

for key in "${!settings[@]}"; do

  grep_config=`cat ~/.gitconfig | grep ${settings[$key]}`

  if [[ ! ${#check_username} > 0 ]]; then
    echo "Your git $key is not set to ${settings[$key]}!"
    echo "Running git config --global user.$key ${settings[$key]} to set your name"

    git config --global user.$key ${settings[$key]}
  fi

  echo "Your $key is set to ${settings[$key]}"

  printf "\n"
done

echo "Script complete"
