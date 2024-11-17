import { Input } from "@nextui-org/input";

const AuthForm = ({
	loginValue,
	passwordValue,
	handleLoginChange,
	handlePasswordChange,
}) => {
	return (
		<div className="flex flex-col align-middle w-72 h-auto">
			<Input
				size="sm"
				type="text"
				label="Логин"
				value={loginValue}
				onChange={handleLoginChange}
			/>
			<Input
				className="mt-2"
				size="sm"
				type="password"
				label="Пароль"
				value={passwordValue}
				onChange={handlePasswordChange}
			/>
		</div>
	);
};

export default AuthForm;
