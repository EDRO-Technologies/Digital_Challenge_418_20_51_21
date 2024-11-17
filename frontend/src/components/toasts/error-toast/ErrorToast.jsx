import { useEffect } from "react";

const ErrorToast = ({ message, onClose }) => {
	useEffect(() => {
		const timer = setTimeout(() => {
			onClose();
		}, 3000);

		return () => clearTimeout(timer);
	}, [onClose]);

	return (
		<div className="fixed bottom-4 left-4 bg-red-500 text-white px-4 py-2 rounded-md shadow-md animate-fade-in">
			<div className="flex items-center justify-between">
				<p>{message}</p>
				<button
					className="ml-4 text-white hover:text-gray-300 focus:outline-none"
					onClick={onClose}
				>
					<svg
						className="w-5 h-5"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
						xmlns="http://www.w3.org/2000/svg"
					>
						<path
							strokeLinecap="round"
							strokeLinejoin="round"
							strokeWidth={2}
							d="M6 18L18 6M6 6l12 12"
						/>
					</svg>
				</button>
			</div>
		</div>
	);
};

export default ErrorToast;
