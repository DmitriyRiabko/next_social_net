import type { PropsWithChildren } from "react";
import Sidebar from "./sidebar/Sidebar";
import styles from "./Layout.module.scss"

export default function LayoutClient({ children }: PropsWithChildren) {
  return (
    <main className={styles.layout}>
      <Sidebar />
      <section>{children}</section>
    </main>
  );
}
