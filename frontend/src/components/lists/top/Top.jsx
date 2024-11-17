import { Button } from "@nextui-org/button";
import { Listbox, ListboxItem } from "@nextui-org/listbox";
import { useState } from "react";
import ListboxWrapper from "./ListboxWrapper";

const Top = ({ productive, energyIntensive }) => {
	const [currentTop, setCurrentTop] = useState("productive");
	return (
		<div className="border-small rounded-md border-solid border-[#e5e5e5] h-96">
			<div className="flex m-2 gap-1">
				<Button
					className="w-32"
					size="sm"
					color="primary"
					variant="light"
					onClick={() => setCurrentTop("productive")}
				>
					Производит.
				</Button>
				<Button
					className="w-32"
					size="sm"
					color="primary"
					variant="light"
					onClick={() => setCurrentTop("energyIntensive")}
				>
					Энергозатр.
				</Button>
			</div>
			<ListboxWrapper>
				<Listbox
					aria-label="Listbox Variants"
					color="default"
					variant="flat"
					classNames={{
						list: "max-h-80 overflow-scroll",
					}}
				>
					{currentTop == "productive" &&
						productive.map((obj, i) => (
							<ListboxItem key={i}>{name}</ListboxItem>
						))}
					{currentTop == "energyIntensive" &&
						energyIntensive.map((obj, i) => (
							<ListboxItem key={i}>{obj}</ListboxItem>
						))}
				</Listbox>
			</ListboxWrapper>
		</div>
	);
};

export default Top;
