import { Button } from "@nextui-org/react";
import { useState } from "react";
import sngLogoSrc from "../../assets/sng-logo.png";
import ErrorToast from "../../components/toasts/error-toast/ErrorToast";
import { useLogin } from "../../hooks/auth/useLogin";
import AuthForm from "../../layouts/auth/auth";

const AuthView = () => {
	const [showToast, setShowToast] = useState(false);
	const [errorMessage, setErrorMessage] = useState("");

	const showErrorToast = message => {
		setErrorMessage(message);
		setShowToast(true);
	};

	const handleClose = () => {
		setShowToast(false);
	};

	const [loginValue, setLoginValue] = useState("");
	const [passwordValue, setPasswordValue] = useState("");

	const handleLoginChange = event => {
		setLoginValue(event.target.value);
	};
	const handlePasswordChange = event => {
		setPasswordValue(event.target.value);
	};

	const { loginRefetch } = useLogin(loginValue, passwordValue, showErrorToast);

	const handleLoginClick = () => {
		loginRefetch();
	};

	return (
		<form className="w-full h-full flex flex-col items-center justify-center">
			<img className="w-36" src={sngLogoSrc} alt="sng-logo" />
			<h1 className="mt-5 mb-5">Аутентификация</h1>
			<AuthForm
				loginValue={loginValue}
				passwordValue={passwordValue}
				handleLoginChange={handleLoginChange}
				handlePasswordChange={handlePasswordChange}
			/>
			<Button
				className="w-72 mt-10"
				size="md"
				color="primary"
				variant="flat"
				onClick={() => handleLoginClick()}
			>
				Войти
			</Button>
			{showToast && <ErrorToast message={errorMessage} onClose={handleClose} />}
		</form>
	);
};

export default AuthView;
