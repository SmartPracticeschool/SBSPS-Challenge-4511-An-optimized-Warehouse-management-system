<?php include('server.php') ?>
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Login/Registration</title>
  <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Open+Sans'>
  <link rel="stylesheet" href="style.css">
  <style type="text/css">
    body{
      background: url('back.jfif') no-repeat center fixed;     
      background-size: cover;
    }
  </style>
</head>
<body>
<!-- partial:index.partial.html -->
<p class="tip"></p>
<div class="cont" style="border-radius: 30px; box-shadow: 0 30px 100px -12px rgba(122, 161, 186, 0.5); ">
  <form class="form sign-in" action="register.php" method="post">
    <h2>Welcome back,</h2>
    <?php include('errors.php'); ?>
    <label>
      <span>Username</span>
      <input type="text" name="username"/>
    </label>
    <label>
      <span>Password</span>
      <input type="password" name="password" />
    </label>
    <p class="forgot-pass"></p>
    <button type="submit" class="submit" name="login_user">Sign In</button>
  </form>
  <div class="sub-cont">
    <div class="img">
      <div class="img__text m--up">
        <h2>New here?</h2>
        <p>Sign up and Explore!</p>
      </div>
      <div class="img__text m--in">
        <h2>One of us?</h2>
        <p>Already have an account</p>
      </div>
      <div class="img__btn">
        <span class="m--up">Sign Up</span>
        <span class="m--in">Sign In</span>
      </div>
    </div>
    <form class="form sign-up" action="register.php" method="post">
      <?php include('errors.php'); ?>
      <h2>Fill the below fields</h2>
      <label>
        <span>Name</span>
        <input type="text" name="username" value="<?php echo $username; ?>"/>
      </label>
      <label>
        <span>Email</span>
        <input type="email" name="email" value="<?php echo $email; ?>"/>
      </label>
      <label>
        <span>Password</span>
        <input type="password" name="password_1" />
      </label>
      <label>
        <span>Password</span>
        <input type="password" name="password_2"/>
      </label>
      <button type="submit" class="submit" name="reg_user">Sign Up</button>
    </form>
  </div>
</div>
  
<!-- partial -->
  <script  src="./script.js"></script>

</body>
</html>
