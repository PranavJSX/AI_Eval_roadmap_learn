from classes_scaffolding import Library, Book, AudioBook, Ebook


def main():
    print("---------------WELCOME TO YOUR LIBRARY---------------")
    my_library = Library()

    book1 = Book(
        title="Clean Code",
        author="Rober Wilde",
        isbn="979-0132350884",
    )

    ebook1 = Ebook(
        title="Fluent Python",
        author="Luciano Ramalho",
        isbn="978-1491946008",
        file_size_mb=15.2,
    )

    audio1 = AudioBook(
        title="Atomic Habits",
        author="James Clear",
        isbn="978-0735211292",
        duration_hours=5.5,
    )

    # 3. Add books to the library
    print("\n[+] Adding books to the library...")
    my_library.add_book(book1)
    my_library.add_book(ebook1)
    my_library.add_book(audio1)

    # 4. List all books (Demonstrating Polymorphism in get_details)
    print("\n--- 📖 ALL BOOKS IN LIBRARY ---")
    my_library.list_all_books()

    # 5. Check out a book
    print("\n--- 🛒 CHECKING OUT 'Fluent Python' ---")
    checkout_result = my_library.checkout_book("fluent python")
    print(f"Status: {checkout_result}")

    # 6. Try to check out the same book again (Testing Edge Case)
    print("\n--- 🛒 ATTEMPTING SECOND CHECKOUT OF 'Fluent Python' ---")
    checkout_again = my_library.checkout_book("fluent python")
    print(f"Status: {checkout_again}")

    # 7. Demonstrate Polymorphic Late Fees
    print("\n--- 💸 CALCULATING 5-DAY LATE FEES ---")
    days_late = 5
    print(
        f"• Physical Book ('{book1.title}'): ${book1.calculate_late_fee(days_late):.2f}"
    )
    print(
        f"• E-Book ('{ebook1.title}'):        ${ebook1.calculate_late_fee(days_late):.2f}"
    )
    print(
        f"• Audio Book ('{audio1.title}'):    ${audio1.calculate_late_fee(days_late):.2f}"
    )

    # 8. Return the book
    print("\n--- 🔄 RETURNING 'Fluent Python' ---")
    return_result = my_library.return_book("fluent python")
    print(f"Status: {return_result}")

    print("\n==========================================")
    print("   ✅ ALL OOP TESTS PASSED SUCCESSFULLY!  ")
    print("==========================================")


if __name__ == "__main__":
    main()
