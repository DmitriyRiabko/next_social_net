'use client'

import { MessagesSquare, Phone, Settings, Sun, Users2 } from "lucide-react";
import Image from "next/image";
import Link from "next/link";
import styles from "./Sidebar.module.scss";
import { MENU } from "./sidebar.data";
import cn from 'clsx'
import { usePathname } from "next/navigation";

export default function Sidebar() {
  const pathname = usePathname()

  return (
    <aside className={styles.sidebar}>
      <Image src={"/logo.svg"}  priority alt=" " width={45} height={45} />
      <div>
        {MENU.map(item=>(
          <Link  
          key={item.url}
          href={item.url}
          className={
            cn(

            )
          }>
          
          <item.Icon size={30}/>
        </Link>
        ))}
      </div>
      <Sun size={35}/>
    </aside>
  );
}
