function is_exsit() {
  file_path="/etc/profile"
  dir_path="/etc/ssh/"
  relative_path="./.env"
  # flag -f assert file
  if [[ -f $file_path ]];then
    echo "$file_path exist"
  else
    echo "$file_path not exist"
  fi

  # flag -d assert directory
  if [[ -d $dir_path ]];then
    echo "$dir_path exist"
  else
    echo "$dir_path not exist"
  fi

  if [[ -f $relative_path ]];then
    echo "$relative_path exist"
  else
    echo "$relative_path not exist"
  fi
}

is_exsit